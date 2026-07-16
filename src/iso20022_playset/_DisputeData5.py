# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Exact1NumericText
from . import Max20Text
from . import Max35Text
from . import Max50Text
from . import TrueFalseIndicator

class DisputeData5(base_types._BaseFieldType):

	__slots__ = ["_AcqrrCaseRef", "_AgtBndlCaseRef", "_AgtCaseRef", "_ChrgbckElgblty", "_Cond", "_Cycl", "_DcmnttnSts", "_IssrCaseRef", "_MsgTxt", "_NtlData", "_Prtl", "_PrvtData", "_RjctRsn", "_Sts"]
	@property
	def AcqrrCaseRef(self):
		return self._AcqrrCaseRef

	@AcqrrCaseRef.setter
	def AcqrrCaseRef(self, value):
		self._AcqrrCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AcqrrCaseRef', Max20Text, False)

	@AcqrrCaseRef.deleter
	def AcqrrCaseRef(self):
		del self._AcqrrCaseRef
		self._AcqrrCaseRef = base_types.UninitialisedField(self, 'AcqrrCaseRef', Max20Text, False)

	@property
	def AgtBndlCaseRef(self):
		return self._AgtBndlCaseRef

	@AgtBndlCaseRef.setter
	def AgtBndlCaseRef(self, value):
		self._AgtBndlCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AgtBndlCaseRef', Max20Text, False)

	@AgtBndlCaseRef.deleter
	def AgtBndlCaseRef(self):
		del self._AgtBndlCaseRef
		self._AgtBndlCaseRef = base_types.UninitialisedField(self, 'AgtBndlCaseRef', Max20Text, False)

	@property
	def AgtCaseRef(self):
		return self._AgtCaseRef

	@AgtCaseRef.setter
	def AgtCaseRef(self, value):
		self._AgtCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AgtCaseRef', Max20Text, False)

	@AgtCaseRef.deleter
	def AgtCaseRef(self):
		del self._AgtCaseRef
		self._AgtCaseRef = base_types.UninitialisedField(self, 'AgtCaseRef', Max20Text, False)

	@property
	def ChrgbckElgblty(self):
		return self._ChrgbckElgblty

	@ChrgbckElgblty.setter
	def ChrgbckElgblty(self, value):
		self._ChrgbckElgblty = value if value is not None else base_types.UninitialisedField(self, 'ChrgbckElgblty', Max35Text, False)

	@ChrgbckElgblty.deleter
	def ChrgbckElgblty(self):
		del self._ChrgbckElgblty
		self._ChrgbckElgblty = base_types.UninitialisedField(self, 'ChrgbckElgblty', Max35Text, False)

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if value is not None else base_types.UninitialisedField(self, 'Cond', Max35Text, False)

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = base_types.UninitialisedField(self, 'Cond', Max35Text, False)

	@property
	def Cycl(self):
		return self._Cycl

	@Cycl.setter
	def Cycl(self, value):
		self._Cycl = value if value is not None else base_types.UninitialisedField(self, 'Cycl', Exact1NumericText, False)

	@Cycl.deleter
	def Cycl(self):
		del self._Cycl
		self._Cycl = base_types.UninitialisedField(self, 'Cycl', Exact1NumericText, False)

	@property
	def DcmnttnSts(self):
		return self._DcmnttnSts

	@DcmnttnSts.setter
	def DcmnttnSts(self, value):
		self._DcmnttnSts = value if value is not None else base_types.UninitialisedField(self, 'DcmnttnSts', Max35Text, False)

	@DcmnttnSts.deleter
	def DcmnttnSts(self):
		del self._DcmnttnSts
		self._DcmnttnSts = base_types.UninitialisedField(self, 'DcmnttnSts', Max35Text, False)

	@property
	def IssrCaseRef(self):
		return self._IssrCaseRef

	@IssrCaseRef.setter
	def IssrCaseRef(self, value):
		self._IssrCaseRef = value if value is not None else base_types.UninitialisedField(self, 'IssrCaseRef', Max20Text, False)

	@IssrCaseRef.deleter
	def IssrCaseRef(self):
		del self._IssrCaseRef
		self._IssrCaseRef = base_types.UninitialisedField(self, 'IssrCaseRef', Max20Text, False)

	@property
	def MsgTxt(self):
		return self._MsgTxt

	@MsgTxt.setter
	def MsgTxt(self, value):
		self._MsgTxt = value if value is not None else base_types.UninitialisedField(self, 'MsgTxt', Max50Text, False)

	@MsgTxt.deleter
	def MsgTxt(self):
		del self._MsgTxt
		self._MsgTxt = base_types.UninitialisedField(self, 'MsgTxt', Max50Text, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def Prtl(self):
		return self._Prtl

	@Prtl.setter
	def Prtl(self, value):
		self._Prtl = value if value is not None else base_types.UninitialisedField(self, 'Prtl', TrueFalseIndicator, False)

	@Prtl.deleter
	def Prtl(self):
		del self._Prtl
		self._Prtl = base_types.UninitialisedField(self, 'Prtl', TrueFalseIndicator, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctRsn', Max35Text, True)

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = base_types.UninitialisedField(self, 'RjctRsn', Max35Text, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Max35Text, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtBndlCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgbckElgblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmnttnSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgTxt', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prtl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RjctRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))