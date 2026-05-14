# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovements6 import IntraPositionMovements6
from ._IntraPositionReport4 import IntraPositionReport4
from ._Pagination1 import Pagination1

class IntraPositionMovementQueryResponseV01(base_types._BaseFieldType):

	__slots__ = ["_Mvmnts", "_Pgntn", "_RptGnlDtls"]
	@property
	def Mvmnts(self):
		return self._Mvmnts

	@Mvmnts.setter
	def Mvmnts(self, value):
		self._Mvmnts = value if type(value) != base_types.auto else self.make_default("Mvmnts")

	@Mvmnts.deleter
	def Mvmnts(self):
		del self._Mvmnts
		self._Mvmnts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnts', type=IntraPositionMovements6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=IntraPositionReport4, min=1, max=1, mutex_group=None, array=False),
	))