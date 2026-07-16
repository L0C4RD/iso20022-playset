# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OpeningBalance7Choice
from . import ShortLong1Code

class OpeningBalance6(base_types._BaseFieldType):

	__slots__ = ["_OpngBal", "_ShrtLngInd"]
	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if value is not None else base_types.UninitialisedField(self, 'OpngBal', OpeningBalance7Choice, False)

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = base_types.UninitialisedField(self, 'OpngBal', OpeningBalance7Choice, False)

	@property
	def ShrtLngInd(self):
		return self._ShrtLngInd

	@ShrtLngInd.setter
	def ShrtLngInd(self, value):
		self._ShrtLngInd = value if value is not None else base_types.UninitialisedField(self, 'ShrtLngInd', ShortLong1Code, False)

	@ShrtLngInd.deleter
	def ShrtLngInd(self):
		del self._ShrtLngInd
		self._ShrtLngInd = base_types.UninitialisedField(self, 'ShrtLngInd', ShortLong1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))