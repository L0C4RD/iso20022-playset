# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max105Text
from . import StatusReason4Choice
from . import TechnicalValidationStatus1Code

class ValidationStatusInformation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsRsnInf", "_Sts", "_StsRsn"]
	@property
	def AddtlStsRsnInf(self):
		return self._AddtlStsRsnInf

	@AddtlStsRsnInf.setter
	def AddtlStsRsnInf(self, value):
		self._AddtlStsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlStsRsnInf', Max105Text, True)

	@AddtlStsRsnInf.deleter
	def AddtlStsRsnInf(self):
		del self._AddtlStsRsnInf
		self._AddtlStsRsnInf = base_types.UninitialisedField(self, 'AddtlStsRsnInf', Max105Text, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', TechnicalValidationStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', TechnicalValidationStatus1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', StatusReason4Choice, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', StatusReason4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=TechnicalValidationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReason4Choice, min=0, max=1, mutex_group=None, array=False),
	))