"""
Implementation of Circular Buffer in python.
It can hold mixed data type of fixed capacity.
I would have used array.array or bytearray but that limits us to fixed data type.
"""

from typing import Any


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Buffer capacity cannot be less than 1")

        self.capacity = capacity

        self._buffer: list[Any] = [None] * self.capacity

        self._buf_len = 0
        self._buf_writer_pointer = 0  # where to currently write to
        self._buf_reader_pointer = 0  # from where to currently read

    def _advance_reader_pointer(self) -> None:
        self._buf_reader_pointer = (self._buf_reader_pointer + 1) % self.capacity

    def _advance_writer_pointer(self) -> None:
        self._buf_writer_pointer = (self._buf_writer_pointer + 1) % self.capacity

    def _write_data(self, data: Any) -> None:
        self._buffer[self._buf_writer_pointer] = data
        self._advance_writer_pointer()

    def _read_data(self) -> Any:
        data = self._buffer[self._buf_reader_pointer]
        self._advance_reader_pointer()

        return data

    def read(self) -> Any:
        if self._buf_len == 0:
            raise BufferEmptyException("Circular buffer is empty")

        self._buf_len -= 1  # free up space
        return self._read_data()

    def write(self, data: Any) -> None:
        if self._buf_len == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self._buf_len += 1
        self._write_data(data)

    def overwrite(self, data: Any) -> None:
        if self._buf_len == self.capacity:  # overwriting
            self._advance_reader_pointer()  # move the reader pointer ahead when overwriting
            self._write_data(data)
        else:
            self.write(data)

    def clear(self) -> None:
        self._buf_writer_pointer = self._buf_reader_pointer = self._buf_len = 0
