# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2
from . import ShortLong1Code

class TotalVariationMargin1(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_ShrtLngInd"]
	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', Amount2, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', Amount2, False)

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
		base_types.FieldEntry(name='AmtDtls', type=Amount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
	))