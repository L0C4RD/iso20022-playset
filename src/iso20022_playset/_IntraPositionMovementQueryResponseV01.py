# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovements6
from . import IntraPositionReport4
from . import Pagination1

class IntraPositionMovementQueryResponseV01(base_types._BaseFieldType):

	__slots__ = ["_Mvmnts", "_Pgntn", "_RptGnlDtls"]
	@property
	def Mvmnts(self):
		return self._Mvmnts

	@Mvmnts.setter
	def Mvmnts(self, value):
		self._Mvmnts = value if value is not None else base_types.UninitialisedField(self, 'Mvmnts', IntraPositionMovements6, True)

	@Mvmnts.deleter
	def Mvmnts(self):
		del self._Mvmnts
		self._Mvmnts = base_types.UninitialisedField(self, 'Mvmnts', IntraPositionMovements6, True)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', IntraPositionReport4, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', IntraPositionReport4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnts', type=IntraPositionMovements6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=IntraPositionReport4, min=1, max=1, mutex_group=None, array=False),
	))