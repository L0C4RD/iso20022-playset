# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosingBalance6Choice
from . import ShortLong1Code

class ClosingBalance5(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_ShrtLngInd"]
	@property
	def ClsgBal(self):
		return self._ClsgBal

	@ClsgBal.setter
	def ClsgBal(self, value):
		self._ClsgBal = value if value is not None else base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance6Choice, False)

	@ClsgBal.deleter
	def ClsgBal(self):
		del self._ClsgBal
		self._ClsgBal = base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance6Choice, False)

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
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))