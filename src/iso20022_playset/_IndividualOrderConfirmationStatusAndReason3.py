# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ConfirmationStatus1Choice import ConfirmationStatus1Choice
from ._FinancialInstrument107 import FinancialInstrument107
from ._InvestmentAccount81 import InvestmentAccount81
from ._Max35Text import Max35Text
from ._PartyIdentification139 import PartyIdentification139

class IndividualOrderConfirmationStatusAndReason3(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_Conf", "_DealRef", "_FinInstrmDtls", "_InvstmtAcctDtls", "_MstrRef", "_NonceId", "_OrdrRef", "_StsInitr"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if type(value) != base_types.auto else self.make_default("Conf")

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = None

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if type(value) != base_types.auto else self.make_default("DealRef")

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if type(value) != base_types.auto else self.make_default("NonceId")

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != base_types.auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != base_types.auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Conf', type=ConfirmationStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))