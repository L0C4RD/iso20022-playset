# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyAccount3
from . import LoyaltyAmount1
from . import LoyaltyRebates1
from . import LoyaltyServerData1

class LoyaltyResult3(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Amt", "_Rbts", "_SvrData"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', LoyaltyAccount3, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', LoyaltyAccount3, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', LoyaltyAmount1, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', LoyaltyAmount1, False)

	@property
	def Rbts(self):
		return self._Rbts

	@Rbts.setter
	def Rbts(self, value):
		self._Rbts = value if value is not None else base_types.UninitialisedField(self, 'Rbts', LoyaltyRebates1, False)

	@Rbts.deleter
	def Rbts(self):
		del self._Rbts
		self._Rbts = base_types.UninitialisedField(self, 'Rbts', LoyaltyRebates1, False)

	@property
	def SvrData(self):
		return self._SvrData

	@SvrData.setter
	def SvrData(self, value):
		self._SvrData = value if value is not None else base_types.UninitialisedField(self, 'SvrData', LoyaltyServerData1, False)

	@SvrData.deleter
	def SvrData(self):
		del self._SvrData
		self._SvrData = base_types.UninitialisedField(self, 'SvrData', LoyaltyServerData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=LoyaltyAccount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=LoyaltyAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rbts', type=LoyaltyRebates1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrData', type=LoyaltyServerData1, min=0, max=1, mutex_group=None, array=False),
	))