# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceContext1Code
from . import Max35Text

class SaleTerminalData1(base_types._BaseFieldType):

	__slots__ = ["_SaleRcncltnId", "_TermnlEnvt"]
	@property
	def SaleRcncltnId(self):
		return self._SaleRcncltnId

	@SaleRcncltnId.setter
	def SaleRcncltnId(self, value):
		self._SaleRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

	@SaleRcncltnId.deleter
	def SaleRcncltnId(self):
		del self._SaleRcncltnId
		self._SaleRcncltnId = base_types.UninitialisedField(self, 'SaleRcncltnId', Max35Text, False)

	@property
	def TermnlEnvt(self):
		return self._TermnlEnvt

	@TermnlEnvt.setter
	def TermnlEnvt(self, value):
		self._TermnlEnvt = value if value is not None else base_types.UninitialisedField(self, 'TermnlEnvt', AttendanceContext1Code, False)

	@TermnlEnvt.deleter
	def TermnlEnvt(self):
		del self._TermnlEnvt
		self._TermnlEnvt = base_types.UninitialisedField(self, 'TermnlEnvt', AttendanceContext1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlEnvt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
	))