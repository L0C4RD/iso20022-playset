# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentIdentification51 import DocumentIdentification51
from ._IntraBalanceOrOperationalError10Choice import IntraBalanceOrOperationalError10Choice
from ._IntraBalanceReport5 import IntraBalanceReport5
from ._Pagination1 import Pagination1
from ._SupplementaryData1 import SupplementaryData1

class IntraBalanceMovementCancellationReportV02(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Pgntn", "_RptGnlDtls", "_RptOrErr", "_SplmtryData"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != base_types.auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

	@property
	def RptOrErr(self):
		return self._RptOrErr

	@RptOrErr.setter
	def RptOrErr(self, value):
		self._RptOrErr = value if type(value) != base_types.auto else self.make_default("RptOrErr")

	@RptOrErr.deleter
	def RptOrErr(self):
		del self._RptOrErr
		self._RptOrErr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentIdentification51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=IntraBalanceReport5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptOrErr', type=IntraBalanceOrOperationalError10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))