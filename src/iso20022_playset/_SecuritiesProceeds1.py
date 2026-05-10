from . import base_types
from ._SecuritiesAccount10 import SecuritiesAccount10
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice
from ._Max350Text import Max350Text
from ._SecurityIdentification7 import SecurityIdentification7

class SecuritiesProceeds1(base_types._BaseFieldType):

	__slots__ = ["_PstngQty", "_RcncltnDtls", "_AcctDtls", "_SctyId"]
	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if type(value) != base_types.auto else self.make_default("PstngQty")

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = None

	@property
	def RcncltnDtls(self):
		return self._RcncltnDtls

	@RcncltnDtls.setter
	def RcncltnDtls(self, value):
		self._RcncltnDtls = value if type(value) != base_types.auto else self.make_default("RcncltnDtls")

	@RcncltnDtls.deleter
	def RcncltnDtls(self):
		del self._RcncltnDtls
		self._RcncltnDtls = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstngQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount10, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))

