# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import DisputeReference1
from . import Exact1NumericText
from . import Max35Text
from . import TrueFalseIndicator

class DisputeData4(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_ChrgbckElgblty", "_Cond", "_Cycl", "_DcmnttnSts", "_Prtl", "_Ref", "_RjctRsn", "_Sts"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

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
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', DisputeReference1, True)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', DisputeReference1, True)

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
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgbckElgblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmnttnSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=DisputeReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RjctRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))