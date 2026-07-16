# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalInvestigationStatus1Code
from . import InvestigationStatusReason1Choice

class InvestigationStatus2(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_StsRsn"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ExternalInvestigationStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ExternalInvestigationStatus1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', InvestigationStatusReason1Choice, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', InvestigationStatusReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=ExternalInvestigationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=InvestigationStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))