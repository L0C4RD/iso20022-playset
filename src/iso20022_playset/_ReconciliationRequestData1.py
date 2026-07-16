# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ReconciliationType1Code

class ReconciliationRequestData1(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_POIRcncltnId", "_RcncltnTp"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@property
	def RcncltnTp(self):
		return self._RcncltnTp

	@RcncltnTp.setter
	def RcncltnTp(self, value):
		self._RcncltnTp = value if value is not None else base_types.UninitialisedField(self, 'RcncltnTp', ReconciliationType1Code, False)

	@RcncltnTp.deleter
	def RcncltnTp(self):
		del self._RcncltnTp
		self._RcncltnTp = base_types.UninitialisedField(self, 'RcncltnTp', ReconciliationType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTp', type=ReconciliationType1Code, min=1, max=1, mutex_group=None, array=False),
	))