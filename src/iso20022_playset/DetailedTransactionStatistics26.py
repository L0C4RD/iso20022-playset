import base_types
import MissingMarginData2
import Number

class DetailedTransactionStatistics26(base_types._BaseFieldType):

	__slots__ = ["_NbOfOutsdngDerivs", "_Wrnngs", "_NbOfOutsdngDerivsWthOutdtdMrgnInf", "_NbOfOutsdngDerivsWthNoMrgnInf"]
	@property
	def NbOfOutsdngDerivs(self):
		return self._NbOfOutsdngDerivs

	@NbOfOutsdngDerivs.setter
	def NbOfOutsdngDerivs(self, value):
		self._NbOfOutsdngDerivs = value if type(value) != auto else self.make_default("NbOfOutsdngDerivs")

	@NbOfOutsdngDerivs.deleter
	def NbOfOutsdngDerivs(self):
		del self._NbOfOutsdngDerivs
		self._NbOfOutsdngDerivs = None

	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if type(value) != auto else self.make_default("Wrnngs")

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = None

	@property
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		return self._NbOfOutsdngDerivsWthOutdtdMrgnInf

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.setter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = value if type(value) != auto else self.make_default("NbOfOutsdngDerivsWthOutdtdMrgnInf")

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.deleter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		del self._NbOfOutsdngDerivsWthOutdtdMrgnInf
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = None

	@property
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		return self._NbOfOutsdngDerivsWthNoMrgnInf

	@NbOfOutsdngDerivsWthNoMrgnInf.setter
	def NbOfOutsdngDerivsWthNoMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthNoMrgnInf = value if type(value) != auto else self.make_default("NbOfOutsdngDerivsWthNoMrgnInf")

	@NbOfOutsdngDerivsWthNoMrgnInf.deleter
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		del self._NbOfOutsdngDerivsWthNoMrgnInf
		self._NbOfOutsdngDerivsWthNoMrgnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrnngs', type=MissingMarginData2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

