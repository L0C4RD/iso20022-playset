from . import base_types
from .Quantity51Choice import Quantity51Choice
from .SafekeepingPlaceFormat42Choice import SafekeepingPlaceFormat42Choice
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .PartyIdentification127Choice import PartyIdentification127Choice
from .CorporateActionOption41Choice import CorporateActionOption41Choice
from .SecurityIdentification19 import SecurityIdentification19
from .Max35Text import Max35Text
from .OptionFeaturesFormat25Choice import OptionFeaturesFormat25Choice
from .OptionNumber1Choice import OptionNumber1Choice
from .SignedQuantityFormat11 import SignedQuantityFormat11
from .CashAccountIdentification9Choice import CashAccountIdentification9Choice
from .Max140Text import Max140Text

class CorporateActionOption239(base_types._BaseFieldType):

	__slots__ = ["_SfkpgAcct", "_StsQty", "_AcctOwnr", "_SfkpgPlc", "_BlckChainAdrOrWllt", "_FinInstrmId", "_OptnNb", "_CshAcct", "_TtlElgblBal", "_StsCshAmt", "_OptnTp", "_UinstdBal", "_PrtctBal", "_OptnFeatrs", "_InstdBal"]
	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def StsQty(self):
		return self._StsQty

	@StsQty.setter
	def StsQty(self, value):
		self._StsQty = value if type(value) != base_types.auto else self.make_default("StsQty")

	@StsQty.deleter
	def StsQty(self):
		del self._StsQty
		self._StsQty = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if type(value) != base_types.auto else self.make_default("TtlElgblBal")

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = None

	@property
	def StsCshAmt(self):
		return self._StsCshAmt

	@StsCshAmt.setter
	def StsCshAmt(self, value):
		self._StsCshAmt = value if type(value) != base_types.auto else self.make_default("StsCshAmt")

	@StsCshAmt.deleter
	def StsCshAmt(self):
		del self._StsCshAmt
		self._StsCshAmt = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if type(value) != base_types.auto else self.make_default("UinstdBal")

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = None

	@property
	def PrtctBal(self):
		return self._PrtctBal

	@PrtctBal.setter
	def PrtctBal(self, value):
		self._PrtctBal = value if type(value) != base_types.auto else self.make_default("PrtctBal")

	@PrtctBal.deleter
	def PrtctBal(self):
		del self._PrtctBal
		self._PrtctBal = None

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if type(value) != base_types.auto else self.make_default("OptnFeatrs")

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = None

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if type(value) != base_types.auto else self.make_default("InstdBal")

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctBal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=None, array=False),
	))

