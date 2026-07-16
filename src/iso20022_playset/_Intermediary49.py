# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account35
from . import InvestmentFundRole2Choice
from . import OrderOriginatorEligibility1Code
from . import PartyIdentification139
from . import TradingCapacity8Code

class Intermediary49(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_OrdrOrgtrElgblty", "_Role", "_TradgPtyCpcty"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', Account35, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', Account35, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification139, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification139, False)

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if value is not None else base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', InvestmentFundRole2Choice, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', InvestmentFundRole2Choice, False)

	@property
	def TradgPtyCpcty(self):
		return self._TradgPtyCpcty

	@TradgPtyCpcty.setter
	def TradgPtyCpcty(self, value):
		self._TradgPtyCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgPtyCpcty', TradingCapacity8Code, False)

	@TradgPtyCpcty.deleter
	def TradgPtyCpcty(self):
		del self._TradgPtyCpcty
		self._TradgPtyCpcty = base_types.UninitialisedField(self, 'TradgPtyCpcty', TradingCapacity8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification139, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=InvestmentFundRole2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyCpcty', type=TradingCapacity8Code, min=0, max=1, mutex_group=None, array=False),
	))