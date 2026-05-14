# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Exact1NumericText import Exact1NumericText
from ._Max20Text import Max20Text
from ._Max35Text import Max35Text
from ._Max50Text import Max50Text
from ._TrueFalseIndicator import TrueFalseIndicator

class DisputeData5(base_types._BaseFieldType):

	__slots__ = ["_AcqrrCaseRef", "_AgtBndlCaseRef", "_AgtCaseRef", "_ChrgbckElgblty", "_Cond", "_Cycl", "_DcmnttnSts", "_IssrCaseRef", "_MsgTxt", "_NtlData", "_Prtl", "_PrvtData", "_RjctRsn", "_Sts"]
	@property
	def AcqrrCaseRef(self):
		return self._AcqrrCaseRef

	@AcqrrCaseRef.setter
	def AcqrrCaseRef(self, value):
		self._AcqrrCaseRef = value if type(value) != base_types.auto else self.make_default("AcqrrCaseRef")

	@AcqrrCaseRef.deleter
	def AcqrrCaseRef(self):
		del self._AcqrrCaseRef
		self._AcqrrCaseRef = None

	@property
	def AgtBndlCaseRef(self):
		return self._AgtBndlCaseRef

	@AgtBndlCaseRef.setter
	def AgtBndlCaseRef(self, value):
		self._AgtBndlCaseRef = value if type(value) != base_types.auto else self.make_default("AgtBndlCaseRef")

	@AgtBndlCaseRef.deleter
	def AgtBndlCaseRef(self):
		del self._AgtBndlCaseRef
		self._AgtBndlCaseRef = None

	@property
	def AgtCaseRef(self):
		return self._AgtCaseRef

	@AgtCaseRef.setter
	def AgtCaseRef(self, value):
		self._AgtCaseRef = value if type(value) != base_types.auto else self.make_default("AgtCaseRef")

	@AgtCaseRef.deleter
	def AgtCaseRef(self):
		del self._AgtCaseRef
		self._AgtCaseRef = None

	@property
	def ChrgbckElgblty(self):
		return self._ChrgbckElgblty

	@ChrgbckElgblty.setter
	def ChrgbckElgblty(self, value):
		self._ChrgbckElgblty = value if type(value) != base_types.auto else self.make_default("ChrgbckElgblty")

	@ChrgbckElgblty.deleter
	def ChrgbckElgblty(self):
		del self._ChrgbckElgblty
		self._ChrgbckElgblty = None

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != base_types.auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def Cycl(self):
		return self._Cycl

	@Cycl.setter
	def Cycl(self, value):
		self._Cycl = value if type(value) != base_types.auto else self.make_default("Cycl")

	@Cycl.deleter
	def Cycl(self):
		del self._Cycl
		self._Cycl = None

	@property
	def DcmnttnSts(self):
		return self._DcmnttnSts

	@DcmnttnSts.setter
	def DcmnttnSts(self, value):
		self._DcmnttnSts = value if type(value) != base_types.auto else self.make_default("DcmnttnSts")

	@DcmnttnSts.deleter
	def DcmnttnSts(self):
		del self._DcmnttnSts
		self._DcmnttnSts = None

	@property
	def IssrCaseRef(self):
		return self._IssrCaseRef

	@IssrCaseRef.setter
	def IssrCaseRef(self, value):
		self._IssrCaseRef = value if type(value) != base_types.auto else self.make_default("IssrCaseRef")

	@IssrCaseRef.deleter
	def IssrCaseRef(self):
		del self._IssrCaseRef
		self._IssrCaseRef = None

	@property
	def MsgTxt(self):
		return self._MsgTxt

	@MsgTxt.setter
	def MsgTxt(self, value):
		self._MsgTxt = value if type(value) != base_types.auto else self.make_default("MsgTxt")

	@MsgTxt.deleter
	def MsgTxt(self):
		del self._MsgTxt
		self._MsgTxt = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def Prtl(self):
		return self._Prtl

	@Prtl.setter
	def Prtl(self, value):
		self._Prtl = value if type(value) != base_types.auto else self.make_default("Prtl")

	@Prtl.deleter
	def Prtl(self):
		del self._Prtl
		self._Prtl = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if type(value) != base_types.auto else self.make_default("RjctRsn")

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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