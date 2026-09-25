from pathlib import Path
from uuid import UUID, uuid4

from fastapi import UploadFile


STORAGE_ROOT = Path(__file__).resolve().parents[2] / "uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024
ALLOWED_EXTENSIONS = {".pdf", ".doc", ".docx"}


async def save_upload(file: UploadFile, owner_id: UUID) -> Path:
	"""Save an uploaded resume outside the public source tree."""
	original_name = Path(file.filename or "resume").name
	extension = Path(original_name).suffix.lower()
	if extension not in ALLOWED_EXTENSIONS:
		raise ValueError("Only PDF, DOC, and DOCX files are supported")

	owner_directory = STORAGE_ROOT / str(owner_id)
	owner_directory.mkdir(parents=True, exist_ok=True)
	destination = owner_directory / f"{uuid4()}{extension}"
	bytes_written = 0

	try:
		with destination.open("wb") as output:
			while chunk := await file.read(CHUNK_SIZE):
				bytes_written += len(chunk)
				if bytes_written > MAX_FILE_SIZE:
					raise ValueError("File size must not exceed 10 MB")
				output.write(chunk)
	except Exception:
		destination.unlink(missing_ok=True)
		raise
	finally:
		await file.close()

	return destination
