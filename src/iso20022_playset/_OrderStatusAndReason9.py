from . import base_types
from ._CancellationStatus22Choice import CancellationStatus22Choice
from ._Max35Text import Max35Text
from ._PartyIdentification113 import PartyIdentification113

class OrderStatusAndReason9(base_types._BaseFieldType):

	__slots__ = ["_CxlSts", "_MstrRef", "_StsInitr"]
	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if type(value) != base_types.auto else self.make_default("CxlSts")

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != base_types.auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlSts', type=CancellationStatus22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
	))

