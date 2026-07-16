# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExposureMetrics4
from . import Max15NumericText

class VolumeMetrics5(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxs", "_Xpsr"]
	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@property
	def Xpsr(self):
		return self._Xpsr

	@Xpsr.setter
	def Xpsr(self, value):
		self._Xpsr = value if value is not None else base_types.UninitialisedField(self, 'Xpsr', ExposureMetrics4, False)

	@Xpsr.deleter
	def Xpsr(self):
		del self._Xpsr
		self._Xpsr = base_types.UninitialisedField(self, 'Xpsr', ExposureMetrics4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xpsr', type=ExposureMetrics4, min=0, max=1, mutex_group=None, array=False),
	))