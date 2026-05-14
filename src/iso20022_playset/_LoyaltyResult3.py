# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LoyaltyAccount3 import LoyaltyAccount3
from ._LoyaltyAmount1 import LoyaltyAmount1
from ._LoyaltyRebates1 import LoyaltyRebates1
from ._LoyaltyServerData1 import LoyaltyServerData1

class LoyaltyResult3(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Amt", "_Rbts", "_SvrData"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Rbts(self):
		return self._Rbts

	@Rbts.setter
	def Rbts(self, value):
		self._Rbts = value if type(value) != base_types.auto else self.make_default("Rbts")

	@Rbts.deleter
	def Rbts(self):
		del self._Rbts
		self._Rbts = None

	@property
	def SvrData(self):
		return self._SvrData

	@SvrData.setter
	def SvrData(self, value):
		self._SvrData = value if type(value) != base_types.auto else self.make_default("SvrData")

	@SvrData.deleter
	def SvrData(self):
		del self._SvrData
		self._SvrData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=LoyaltyAccount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=LoyaltyAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rbts', type=LoyaltyRebates1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrData', type=LoyaltyServerData1, min=0, max=1, mutex_group=None, array=False),
	))