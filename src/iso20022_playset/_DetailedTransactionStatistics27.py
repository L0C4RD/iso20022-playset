from . import base_types
from ._MissingValuationsData2 import MissingValuationsData2
from ._Number import Number

class DetailedTransactionStatistics27(base_types._BaseFieldType):

	__slots__ = ["_Wrnngs", "_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthNoValtn", "_NbOfOutsdngDerivsWthOutdtdValtn"]
	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if type(value) != base_types.auto else self.make_default("Wrnngs")

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = None

	@property
	def NbOfOutsdngDerivs(self):
		return self._NbOfOutsdngDerivs

	@NbOfOutsdngDerivs.setter
	def NbOfOutsdngDerivs(self, value):
		self._NbOfOutsdngDerivs = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivs")

	@NbOfOutsdngDerivs.deleter
	def NbOfOutsdngDerivs(self):
		del self._NbOfOutsdngDerivs
		self._NbOfOutsdngDerivs = None

	@property
	def NbOfOutsdngDerivsWthNoValtn(self):
		return self._NbOfOutsdngDerivsWthNoValtn

	@NbOfOutsdngDerivsWthNoValtn.setter
	def NbOfOutsdngDerivsWthNoValtn(self, value):
		self._NbOfOutsdngDerivsWthNoValtn = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthNoValtn")

	@NbOfOutsdngDerivsWthNoValtn.deleter
	def NbOfOutsdngDerivsWthNoValtn(self):
		del self._NbOfOutsdngDerivsWthNoValtn
		self._NbOfOutsdngDerivsWthNoValtn = None

	@property
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		return self._NbOfOutsdngDerivsWthOutdtdValtn

	@NbOfOutsdngDerivsWthOutdtdValtn.setter
	def NbOfOutsdngDerivsWthOutdtdValtn(self, value):
		self._NbOfOutsdngDerivsWthOutdtdValtn = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthOutdtdValtn")

	@NbOfOutsdngDerivsWthOutdtdValtn.deleter
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		del self._NbOfOutsdngDerivsWthOutdtdValtn
		self._NbOfOutsdngDerivsWthOutdtdValtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Wrnngs', type=MissingValuationsData2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

