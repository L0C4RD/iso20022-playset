# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccountIdentification5Choice
from . import CreditDebit3Code
from . import Max35Text
from . import ProprietaryStatusAndReason6
from . import YesNoIndicator

class CashMovement7(base_types._BaseFieldType):

	__slots__ = ["_ClntCshMvmntId", "_CollMvmnt", "_CshAcct", "_CshAmt", "_CshMvmnt", "_CshMvmntApprvd", "_MvmntSts", "_PosTp", "_TrptyAgtSvcPrvdrCshMvmntId"]
	@property
	def ClntCshMvmntId(self):
		return self._ClntCshMvmntId

	@ClntCshMvmntId.setter
	def ClntCshMvmntId(self, value):
		self._ClntCshMvmntId = value if value is not None else base_types.UninitialisedField(self, 'ClntCshMvmntId', Max35Text, False)

	@ClntCshMvmntId.deleter
	def ClntCshMvmntId(self):
		del self._ClntCshMvmntId
		self._ClntCshMvmntId = base_types.UninitialisedField(self, 'ClntCshMvmntId', Max35Text, False)

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if value is not None else base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CshMvmnt', CreditDebit3Code, False)

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = base_types.UninitialisedField(self, 'CshMvmnt', CreditDebit3Code, False)

	@property
	def CshMvmntApprvd(self):
		return self._CshMvmntApprvd

	@CshMvmntApprvd.setter
	def CshMvmntApprvd(self, value):
		self._CshMvmntApprvd = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntApprvd', YesNoIndicator, False)

	@CshMvmntApprvd.deleter
	def CshMvmntApprvd(self):
		del self._CshMvmntApprvd
		self._CshMvmntApprvd = base_types.UninitialisedField(self, 'CshMvmntApprvd', YesNoIndicator, False)

	@property
	def MvmntSts(self):
		return self._MvmntSts

	@MvmntSts.setter
	def MvmntSts(self, value):
		self._MvmntSts = value if value is not None else base_types.UninitialisedField(self, 'MvmntSts', ProprietaryStatusAndReason6, False)

	@MvmntSts.deleter
	def MvmntSts(self):
		del self._MvmntSts
		self._MvmntSts = base_types.UninitialisedField(self, 'MvmntSts', ProprietaryStatusAndReason6, False)

	@property
	def PosTp(self):
		return self._PosTp

	@PosTp.setter
	def PosTp(self, value):
		self._PosTp = value if value is not None else base_types.UninitialisedField(self, 'PosTp', YesNoIndicator, False)

	@PosTp.deleter
	def PosTp(self):
		del self._PosTp
		self._PosTp = base_types.UninitialisedField(self, 'PosTp', YesNoIndicator, False)

	@property
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		return self._TrptyAgtSvcPrvdrCshMvmntId

	@TrptyAgtSvcPrvdrCshMvmntId.setter
	def TrptyAgtSvcPrvdrCshMvmntId(self, value):
		self._TrptyAgtSvcPrvdrCshMvmntId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCshMvmntId', Max35Text, False)

	@TrptyAgtSvcPrvdrCshMvmntId.deleter
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		del self._TrptyAgtSvcPrvdrCshMvmntId
		self._TrptyAgtSvcPrvdrCshMvmntId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCshMvmntId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CreditDebit3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntSts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosTp', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))