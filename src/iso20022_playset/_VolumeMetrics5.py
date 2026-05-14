# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExposureMetrics4 import ExposureMetrics4
from ._Max15NumericText import Max15NumericText

class VolumeMetrics5(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxs", "_Xpsr"]
	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != base_types.auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	@property
	def Xpsr(self):
		return self._Xpsr

	@Xpsr.setter
	def Xpsr(self, value):
		self._Xpsr = value if type(value) != base_types.auto else self.make_default("Xpsr")

	@Xpsr.deleter
	def Xpsr(self):
		del self._Xpsr
		self._Xpsr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xpsr', type=ExposureMetrics4, min=0, max=1, mutex_group=None, array=False),
	))