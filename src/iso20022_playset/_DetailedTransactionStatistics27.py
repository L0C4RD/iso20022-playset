# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MissingValuationsData2
from . import Number

class DetailedTransactionStatistics27(base_types._BaseFieldType):

	__slots__ = ["_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthNoValtn", "_NbOfOutsdngDerivsWthOutdtdValtn", "_Wrnngs"]
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
	def NbOfOutsdngDerivsWthNoValtn(self):
		return self._NbOfOutsdngDerivsWthNoValtn

	@NbOfOutsdngDerivsWthNoValtn.setter
	def NbOfOutsdngDerivsWthNoValtn(self, value):
		self._NbOfOutsdngDerivsWthNoValtn = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoValtn', Number, False)

	@NbOfOutsdngDerivsWthNoValtn.deleter
	def NbOfOutsdngDerivsWthNoValtn(self):
		del self._NbOfOutsdngDerivsWthNoValtn
		self._NbOfOutsdngDerivsWthNoValtn = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoValtn', Number, False)

	@property
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		return self._NbOfOutsdngDerivsWthOutdtdValtn

	@NbOfOutsdngDerivsWthOutdtdValtn.setter
	def NbOfOutsdngDerivsWthOutdtdValtn(self, value):
		self._NbOfOutsdngDerivsWthOutdtdValtn = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdValtn', Number, False)

	@NbOfOutsdngDerivsWthOutdtdValtn.deleter
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		del self._NbOfOutsdngDerivsWthOutdtdValtn
		self._NbOfOutsdngDerivsWthOutdtdValtn = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdValtn', Number, False)

	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if value is not None else base_types.UninitialisedField(self, 'Wrnngs', MissingValuationsData2, True)

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = base_types.UninitialisedField(self, 'Wrnngs', MissingValuationsData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrnngs', type=MissingValuationsData2, min=1, max=None, mutex_group=None, array=True),
	))