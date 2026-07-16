# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccount19
from . import Status6Code
from . import StatusReasonInformation10

class SecuritiesAccountStatus2(base_types._BaseFieldType):

	__slots__ = ["_RltdSctiesAcct", "_Sts", "_StsRsn"]
	@property
	def RltdSctiesAcct(self):
		return self._RltdSctiesAcct

	@RltdSctiesAcct.setter
	def RltdSctiesAcct(self, value):
		self._RltdSctiesAcct = value if value is not None else base_types.UninitialisedField(self, 'RltdSctiesAcct', SecuritiesAccount19, False)

	@RltdSctiesAcct.deleter
	def RltdSctiesAcct(self):
		del self._RltdSctiesAcct
		self._RltdSctiesAcct = base_types.UninitialisedField(self, 'RltdSctiesAcct', SecuritiesAccount19, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Status6Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Status6Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation10, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation10, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdSctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation10, min=0, max=None, mutex_group=None, array=True),
	))