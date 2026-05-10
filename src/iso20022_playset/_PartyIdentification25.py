from . import base_types
from ._GenericIdentification4 import GenericIdentification4
from ._Max70Text import Max70Text
from ._BEIIdentifier import BEIIdentifier

class PartyIdentification25(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_BEI", "_PrtryId"]
	@property
	def BEI(self):
		return self._BEI

	@BEI.setter
	def BEI(self, value):
		self._BEI = value if type(value) != base_types.auto else self.make_default("BEI")

	@BEI.deleter
	def BEI(self):
		del self._BEI
		self._BEI = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BEI', type=BEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification4, min=0, max=1, mutex_group=None, array=False),
	))

