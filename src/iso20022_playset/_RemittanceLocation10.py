from . import base_types
from ._Max35Text import Max35Text
from ._RemittanceLocationData2 import RemittanceLocationData2
from ._TransactionReferences8 import TransactionReferences8

class RemittanceLocation10(base_types._BaseFieldType):

	__slots__ = ["_Refs", "_RmtId", "_RmtLctnDtls"]
	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if type(value) != base_types.auto else self.make_default("RmtId")

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = None

	@property
	def RmtLctnDtls(self):
		return self._RmtLctnDtls

	@RmtLctnDtls.setter
	def RmtLctnDtls(self, value):
		self._RmtLctnDtls = value if type(value) != base_types.auto else self.make_default("RmtLctnDtls")

	@RmtLctnDtls.deleter
	def RmtLctnDtls(self):
		del self._RmtLctnDtls
		self._RmtLctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Refs', type=TransactionReferences8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnDtls', type=RemittanceLocationData2, min=1, max=None, mutex_group=None, array=True),
	))

