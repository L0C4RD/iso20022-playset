from . import base_types
from .PartyIdentification136 import PartyIdentification136
from .PartyIdentificationAndAccount202 import PartyIdentificationAndAccount202

class CollateralParties9(base_types._BaseFieldType):

	__slots__ = ["_TrptyAgt", "_PtyA", "_ClntPtyA"]
	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != base_types.auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if type(value) != base_types.auto else self.make_default("PtyA")

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = None

	@property
	def ClntPtyA(self):
		return self._ClntPtyA

	@ClntPtyA.setter
	def ClntPtyA(self, value):
		self._ClntPtyA = value if type(value) != base_types.auto else self.make_default("ClntPtyA")

	@ClntPtyA.deleter
	def ClntPtyA(self):
		del self._ClntPtyA
		self._ClntPtyA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentificationAndAccount202, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntPtyA', type=PartyIdentificationAndAccount202, min=0, max=1, mutex_group=None, array=False),
	))

