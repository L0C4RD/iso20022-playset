# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccount19
from . import YesNoIndicator

class IssuanceAccount2(base_types._BaseFieldType):

	__slots__ = ["_IssncAcct", "_PmryAcctInd"]
	@property
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if value is not None else base_types.UninitialisedField(self, 'IssncAcct', SecuritiesAccount19, False)

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = base_types.UninitialisedField(self, 'IssncAcct', SecuritiesAccount19, False)

	@property
	def PmryAcctInd(self):
		return self._PmryAcctInd

	@PmryAcctInd.setter
	def PmryAcctInd(self, value):
		self._PmryAcctInd = value if value is not None else base_types.UninitialisedField(self, 'PmryAcctInd', YesNoIndicator, False)

	@PmryAcctInd.deleter
	def PmryAcctInd(self):
		del self._PmryAcctInd
		self._PmryAcctInd = base_types.UninitialisedField(self, 'PmryAcctInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssncAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))