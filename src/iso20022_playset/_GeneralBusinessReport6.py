# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GeneralBusinessOrError8Choice
from . import Max35Text

class GeneralBusinessReport6(base_types._BaseFieldType):

	__slots__ = ["_BizInfRef", "_GnlBizOrErr"]
	@property
	def BizInfRef(self):
		return self._BizInfRef

	@BizInfRef.setter
	def BizInfRef(self, value):
		self._BizInfRef = value if value is not None else base_types.UninitialisedField(self, 'BizInfRef', Max35Text, False)

	@BizInfRef.deleter
	def BizInfRef(self):
		del self._BizInfRef
		self._BizInfRef = base_types.UninitialisedField(self, 'BizInfRef', Max35Text, False)

	@property
	def GnlBizOrErr(self):
		return self._GnlBizOrErr

	@GnlBizOrErr.setter
	def GnlBizOrErr(self, value):
		self._GnlBizOrErr = value if value is not None else base_types.UninitialisedField(self, 'GnlBizOrErr', GeneralBusinessOrError8Choice, False)

	@GnlBizOrErr.deleter
	def GnlBizOrErr(self):
		del self._GnlBizOrErr
		self._GnlBizOrErr = base_types.UninitialisedField(self, 'GnlBizOrErr', GeneralBusinessOrError8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizInfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlBizOrErr', type=GeneralBusinessOrError8Choice, min=1, max=1, mutex_group=None, array=False),
	))