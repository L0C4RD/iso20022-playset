# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractBalance1
from . import DocumentGeneralInformation5
from . import Max1025Text
from . import Max35Text
from . import PaymentScheduleType2Choice
from . import Priority2Code
from . import SupplementaryData1
from . import UnderlyingContract4Choice

class RegisteredContract17(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Attchmnt", "_Ctrct", "_CtrctBal", "_OrgnlRegdCtrctId", "_PmtSchdlTp", "_Prty", "_RegdCtrctAmdmntId", "_SplmtryData"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if value is not None else base_types.UninitialisedField(self, 'Ctrct', UnderlyingContract4Choice, False)

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = base_types.UninitialisedField(self, 'Ctrct', UnderlyingContract4Choice, False)

	@property
	def CtrctBal(self):
		return self._CtrctBal

	@CtrctBal.setter
	def CtrctBal(self, value):
		self._CtrctBal = value if value is not None else base_types.UninitialisedField(self, 'CtrctBal', ContractBalance1, True)

	@CtrctBal.deleter
	def CtrctBal(self):
		del self._CtrctBal
		self._CtrctBal = base_types.UninitialisedField(self, 'CtrctBal', ContractBalance1, True)

	@property
	def OrgnlRegdCtrctId(self):
		return self._OrgnlRegdCtrctId

	@OrgnlRegdCtrctId.setter
	def OrgnlRegdCtrctId(self, value):
		self._OrgnlRegdCtrctId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRegdCtrctId', Max35Text, False)

	@OrgnlRegdCtrctId.deleter
	def OrgnlRegdCtrctId(self):
		del self._OrgnlRegdCtrctId
		self._OrgnlRegdCtrctId = base_types.UninitialisedField(self, 'OrgnlRegdCtrctId', Max35Text, False)

	@property
	def PmtSchdlTp(self):
		return self._PmtSchdlTp

	@PmtSchdlTp.setter
	def PmtSchdlTp(self, value):
		self._PmtSchdlTp = value if value is not None else base_types.UninitialisedField(self, 'PmtSchdlTp', PaymentScheduleType2Choice, False)

	@PmtSchdlTp.deleter
	def PmtSchdlTp(self):
		del self._PmtSchdlTp
		self._PmtSchdlTp = base_types.UninitialisedField(self, 'PmtSchdlTp', PaymentScheduleType2Choice, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority2Code, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority2Code, False)

	@property
	def RegdCtrctAmdmntId(self):
		return self._RegdCtrctAmdmntId

	@RegdCtrctAmdmntId.setter
	def RegdCtrctAmdmntId(self, value):
		self._RegdCtrctAmdmntId = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrctAmdmntId', Max35Text, False)

	@RegdCtrctAmdmntId.deleter
	def RegdCtrctAmdmntId(self):
		del self._RegdCtrctAmdmntId
		self._RegdCtrctAmdmntId = base_types.UninitialisedField(self, 'RegdCtrctAmdmntId', Max35Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctrct', type=UnderlyingContract4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctBal', type=ContractBalance1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlRegdCtrctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdlTp', type=PaymentScheduleType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrctAmdmntId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))