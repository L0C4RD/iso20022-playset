# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialPartySectorType2Code
from . import FundType2Code

class FinancialPartyClassification1(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_InvstmtFndClssfctn"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', FinancialPartySectorType2Code, True)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', FinancialPartySectorType2Code, True)

	@property
	def InvstmtFndClssfctn(self):
		return self._InvstmtFndClssfctn

	@InvstmtFndClssfctn.setter
	def InvstmtFndClssfctn(self, value):
		self._InvstmtFndClssfctn = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndClssfctn', FundType2Code, False)

	@InvstmtFndClssfctn.deleter
	def InvstmtFndClssfctn(self):
		del self._InvstmtFndClssfctn
		self._InvstmtFndClssfctn = base_types.UninitialisedField(self, 'InvstmtFndClssfctn', FundType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=FinancialPartySectorType2Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtFndClssfctn', type=FundType2Code, min=0, max=1, mutex_group=None, array=False),
	))