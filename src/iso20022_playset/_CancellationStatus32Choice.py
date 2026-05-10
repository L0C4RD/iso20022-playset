from . import base_types
from ._RejectedStatus31Choice import RejectedStatus31Choice
from ._CancellationProcessingStatus2 import CancellationProcessingStatus2
from ._PendingCancellationStatus12Choice import PendingCancellationStatus12Choice

class CancellationStatus32Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgCxl", "_Rjctd", "_PrcgSts"]
	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != base_types.auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus31Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcgSts', type=CancellationProcessingStatus2, min=0, max=1, mutex_group=1, array=False),
	))

