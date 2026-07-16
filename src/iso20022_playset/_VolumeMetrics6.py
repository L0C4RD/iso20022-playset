# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExposureMetrics5

class VolumeMetrics6(base_types._BaseFieldType):

	__slots__ = ["_Neg", "_Postv"]
	@property
	def Neg(self):
		return self._Neg

	@Neg.setter
	def Neg(self, value):
		self._Neg = value if value is not None else base_types.UninitialisedField(self, 'Neg', ExposureMetrics5, False)

	@Neg.deleter
	def Neg(self):
		del self._Neg
		self._Neg = base_types.UninitialisedField(self, 'Neg', ExposureMetrics5, False)

	@property
	def Postv(self):
		return self._Postv

	@Postv.setter
	def Postv(self, value):
		self._Postv = value if value is not None else base_types.UninitialisedField(self, 'Postv', ExposureMetrics5, False)

	@Postv.deleter
	def Postv(self):
		del self._Postv
		self._Postv = base_types.UninitialisedField(self, 'Postv', ExposureMetrics5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Neg', type=ExposureMetrics5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Postv', type=ExposureMetrics5, min=0, max=1, mutex_group=None, array=False),
	))