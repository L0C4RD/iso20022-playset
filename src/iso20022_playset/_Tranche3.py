# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate

class Tranche3(base_types._BaseFieldType):

	__slots__ = ["_AttchmntPt", "_DtchmntPt"]
	@property
	def AttchmntPt(self):
		return self._AttchmntPt

	@AttchmntPt.setter
	def AttchmntPt(self, value):
		self._AttchmntPt = value if value is not None else base_types.UninitialisedField(self, 'AttchmntPt', BaseOneRate, False)

	@AttchmntPt.deleter
	def AttchmntPt(self):
		del self._AttchmntPt
		self._AttchmntPt = base_types.UninitialisedField(self, 'AttchmntPt', BaseOneRate, False)

	@property
	def DtchmntPt(self):
		return self._DtchmntPt

	@DtchmntPt.setter
	def DtchmntPt(self, value):
		self._DtchmntPt = value if value is not None else base_types.UninitialisedField(self, 'DtchmntPt', BaseOneRate, False)

	@DtchmntPt.deleter
	def DtchmntPt(self):
		del self._DtchmntPt
		self._DtchmntPt = base_types.UninitialisedField(self, 'DtchmntPt', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchmntPt', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchmntPt', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))