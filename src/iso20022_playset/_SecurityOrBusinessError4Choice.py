# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessError4
from . import SecurityAttributes11

class SecurityOrBusinessError4Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_SctyRpt"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', BusinessError4, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', BusinessError4, True)

	@property
	def SctyRpt(self):
		return self._SctyRpt

	@SctyRpt.setter
	def SctyRpt(self, value):
		self._SctyRpt = value if value is not None else base_types.UninitialisedField(self, 'SctyRpt', SecurityAttributes11, True)

	@SctyRpt.deleter
	def SctyRpt(self):
		del self._SctyRpt
		self._SctyRpt = base_types.UninitialisedField(self, 'SctyRpt', SecurityAttributes11, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=BusinessError4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctyRpt', type=SecurityAttributes11, min=1, max=None, mutex_group=1, array=True),
	))