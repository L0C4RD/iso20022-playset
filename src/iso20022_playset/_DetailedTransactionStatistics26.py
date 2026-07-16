# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MissingMarginData2
from . import Number

class DetailedTransactionStatistics26(base_types._BaseFieldType):

	__slots__ = ["_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthNoMrgnInf", "_NbOfOutsdngDerivsWthOutdtdMrgnInf", "_Wrnngs"]
	@property
	def NbOfOutsdngDerivs(self):
		return self._NbOfOutsdngDerivs

	@NbOfOutsdngDerivs.setter
	def NbOfOutsdngDerivs(self, value):
		self._NbOfOutsdngDerivs = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivs', Number, False)

	@NbOfOutsdngDerivs.deleter
	def NbOfOutsdngDerivs(self):
		del self._NbOfOutsdngDerivs
		self._NbOfOutsdngDerivs = base_types.UninitialisedField(self, 'NbOfOutsdngDerivs', Number, False)

	@property
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		return self._NbOfOutsdngDerivsWthNoMrgnInf

	@NbOfOutsdngDerivsWthNoMrgnInf.setter
	def NbOfOutsdngDerivsWthNoMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthNoMrgnInf = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoMrgnInf', Number, False)

	@NbOfOutsdngDerivsWthNoMrgnInf.deleter
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		del self._NbOfOutsdngDerivsWthNoMrgnInf
		self._NbOfOutsdngDerivsWthNoMrgnInf = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoMrgnInf', Number, False)

	@property
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		return self._NbOfOutsdngDerivsWthOutdtdMrgnInf

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.setter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdMrgnInf', Number, False)

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.deleter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		del self._NbOfOutsdngDerivsWthOutdtdMrgnInf
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdMrgnInf', Number, False)

	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if value is not None else base_types.UninitialisedField(self, 'Wrnngs', MissingMarginData2, True)

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = base_types.UninitialisedField(self, 'Wrnngs', MissingMarginData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrnngs', type=MissingMarginData2, min=1, max=None, mutex_group=None, array=True),
	))