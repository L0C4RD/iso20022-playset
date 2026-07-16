# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet3
from . import CashAccount38
from . import DateAndDateTime2Choice
from . import SecuritiesAccount19
from . import YesNoIndicator

class AccountLink7(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_CollstnInd", "_CshAcct", "_CshSttlmInd", "_DfltInd", "_SctiesAcct", "_VldFr", "_VldTo"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def CollstnInd(self):
		return self._CollstnInd

	@CollstnInd.setter
	def CollstnInd(self, value):
		self._CollstnInd = value if value is not None else base_types.UninitialisedField(self, 'CollstnInd', YesNoIndicator, False)

	@CollstnInd.deleter
	def CollstnInd(self):
		del self._CollstnInd
		self._CollstnInd = base_types.UninitialisedField(self, 'CollstnInd', YesNoIndicator, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccount38, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccount38, False)

	@property
	def CshSttlmInd(self):
		return self._CshSttlmInd

	@CshSttlmInd.setter
	def CshSttlmInd(self, value):
		self._CshSttlmInd = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmInd', YesNoIndicator, False)

	@CshSttlmInd.deleter
	def CshSttlmInd(self):
		del self._CshSttlmInd
		self._CshSttlmInd = base_types.UninitialisedField(self, 'CshSttlmInd', YesNoIndicator, False)

	@property
	def DfltInd(self):
		return self._DfltInd

	@DfltInd.setter
	def DfltInd(self, value):
		self._DfltInd = value if value is not None else base_types.UninitialisedField(self, 'DfltInd', YesNoIndicator, False)

	@DfltInd.deleter
	def DfltInd(self):
		del self._DfltInd
		self._DfltInd = base_types.UninitialisedField(self, 'DfltInd', YesNoIndicator, False)

	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcct', SecuritiesAccount19, False)

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = base_types.UninitialisedField(self, 'SctiesAcct', SecuritiesAccount19, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', DateAndDateTime2Choice, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', DateAndDateTime2Choice, False)

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if value is not None else base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = base_types.UninitialisedField(self, 'VldTo', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount38, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))