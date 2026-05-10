from . import base_types
from .YesNoIndicator import YesNoIndicator
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .BlockChainAddressWallet3 import BlockChainAddressWallet3
from .SecuritiesAccount19 import SecuritiesAccount19
from .CashAccount38 import CashAccount38

class AccountLink7(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_CollstnInd", "_DfltInd", "_CshSttlmInd", "_SctiesAcct", "_CshAcct", "_VldFr", "_VldTo"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def CollstnInd(self):
		return self._CollstnInd

	@CollstnInd.setter
	def CollstnInd(self, value):
		self._CollstnInd = value if type(value) != auto else self.make_default("CollstnInd")

	@CollstnInd.deleter
	def CollstnInd(self):
		del self._CollstnInd
		self._CollstnInd = None

	@property
	def DfltInd(self):
		return self._DfltInd

	@DfltInd.setter
	def DfltInd(self, value):
		self._DfltInd = value if type(value) != auto else self.make_default("DfltInd")

	@DfltInd.deleter
	def DfltInd(self):
		del self._DfltInd
		self._DfltInd = None

	@property
	def CshSttlmInd(self):
		return self._CshSttlmInd

	@CshSttlmInd.setter
	def CshSttlmInd(self, value):
		self._CshSttlmInd = value if type(value) != auto else self.make_default("CshSttlmInd")

	@CshSttlmInd.deleter
	def CshSttlmInd(self):
		del self._CshSttlmInd
		self._CshSttlmInd = None

	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if type(value) != auto else self.make_default("SctiesAcct")

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if type(value) != auto else self.make_default("VldTo")

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount38, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

