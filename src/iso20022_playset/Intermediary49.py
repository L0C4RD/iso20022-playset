import base_types
import OrderOriginatorEligibility1Code
import Account35
import InvestmentFundRole2Choice
import PartyIdentification139
import TradingCapacity8Code

class Intermediary49(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Acct", "_TradgPtyCpcty", "_OrdrOrgtrElgblty", "_Role"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def TradgPtyCpcty(self):
		return self._TradgPtyCpcty

	@TradgPtyCpcty.setter
	def TradgPtyCpcty(self, value):
		self._TradgPtyCpcty = value if type(value) != auto else self.make_default("TradgPtyCpcty")

	@TradgPtyCpcty.deleter
	def TradgPtyCpcty(self):
		del self._TradgPtyCpcty
		self._TradgPtyCpcty = None

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if type(value) != auto else self.make_default("OrdrOrgtrElgblty")

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification139, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyCpcty', type=TradingCapacity8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=InvestmentFundRole2Choice, min=0, max=1, mutex_group=None, array=False),
	))

