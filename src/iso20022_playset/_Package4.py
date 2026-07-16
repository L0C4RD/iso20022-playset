# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100Text
from . import SecuritiesTransactionPrice17Choice
from . import SecuritiesTransactionPrice20Choice

class Package4(base_types._BaseFieldType):

	__slots__ = ["_CmplxTradId", "_FxSwpLkId", "_Pric", "_Sprd"]
	@property
	def CmplxTradId(self):
		return self._CmplxTradId

	@CmplxTradId.setter
	def CmplxTradId(self, value):
		self._CmplxTradId = value if value is not None else base_types.UninitialisedField(self, 'CmplxTradId', Max100Text, False)

	@CmplxTradId.deleter
	def CmplxTradId(self):
		del self._CmplxTradId
		self._CmplxTradId = base_types.UninitialisedField(self, 'CmplxTradId', Max100Text, False)

	@property
	def FxSwpLkId(self):
		return self._FxSwpLkId

	@FxSwpLkId.setter
	def FxSwpLkId(self, value):
		self._FxSwpLkId = value if value is not None else base_types.UninitialisedField(self, 'FxSwpLkId', Max100Text, False)

	@FxSwpLkId.deleter
	def FxSwpLkId(self):
		del self._FxSwpLkId
		self._FxSwpLkId = base_types.UninitialisedField(self, 'FxSwpLkId', Max100Text, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice20Choice, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice20Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmplxTradId', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxSwpLkId', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice20Choice, min=0, max=1, mutex_group=None, array=False),
	))