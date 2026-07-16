# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountIdentification10Choice
from . import CorporateActionOption42Choice
from . import OptionFeaturesFormat27Choice
from . import OptionNumber1Choice
from . import PartyIdentification136Choice
from . import Quantity54Choice
from . import RestrictedFINActiveCurrencyAndAmount
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax35Text
from . import SafekeepingPlaceFormat44Choice
from . import SecurityIdentification20
from . import SignedQuantityFormat12

class CorporateActionOption241(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_CshAcct", "_FinInstrmId", "_InstdBal", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_PrtctBal", "_SfkpgAcct", "_SfkpgPlc", "_StsCshAmt", "_StsQty", "_TtlElgblBal", "_UinstdBal"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136Choice, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', RestrictedFINXMax140Text, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', RestrictedFINXMax140Text, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification10Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification10Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if value is not None else base_types.UninitialisedField(self, 'InstdBal', SignedQuantityFormat12, False)

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = base_types.UninitialisedField(self, 'InstdBal', SignedQuantityFormat12, False)

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat27Choice, False)

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat27Choice, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption42Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption42Choice, False)

	@property
	def PrtctBal(self):
		return self._PrtctBal

	@PrtctBal.setter
	def PrtctBal(self, value):
		self._PrtctBal = value if value is not None else base_types.UninitialisedField(self, 'PrtctBal', SignedQuantityFormat12, False)

	@PrtctBal.deleter
	def PrtctBal(self):
		del self._PrtctBal
		self._PrtctBal = base_types.UninitialisedField(self, 'PrtctBal', SignedQuantityFormat12, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', RestrictedFINXMax35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', RestrictedFINXMax35Text, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat44Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat44Choice, False)

	@property
	def StsCshAmt(self):
		return self._StsCshAmt

	@StsCshAmt.setter
	def StsCshAmt(self, value):
		self._StsCshAmt = value if value is not None else base_types.UninitialisedField(self, 'StsCshAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@StsCshAmt.deleter
	def StsCshAmt(self):
		del self._StsCshAmt
		self._StsCshAmt = base_types.UninitialisedField(self, 'StsCshAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def StsQty(self):
		return self._StsQty

	@StsQty.setter
	def StsQty(self, value):
		self._StsQty = value if value is not None else base_types.UninitialisedField(self, 'StsQty', Quantity54Choice, False)

	@StsQty.deleter
	def StsQty(self):
		del self._StsQty
		self._StsQty = base_types.UninitialisedField(self, 'StsQty', Quantity54Choice, False)

	@property
	def TtlElgblBal(self):
		return self._TtlElgblBal

	@TtlElgblBal.setter
	def TtlElgblBal(self, value):
		self._TtlElgblBal = value if value is not None else base_types.UninitialisedField(self, 'TtlElgblBal', SignedQuantityFormat12, False)

	@TtlElgblBal.deleter
	def TtlElgblBal(self):
		del self._TtlElgblBal
		self._TtlElgblBal = base_types.UninitialisedField(self, 'TtlElgblBal', SignedQuantityFormat12, False)

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if value is not None else base_types.UninitialisedField(self, 'UinstdBal', SignedQuantityFormat12, False)

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = base_types.UninitialisedField(self, 'UinstdBal', SignedQuantityFormat12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption42Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctBal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat44Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCshAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlElgblBal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=None, array=False),
	))