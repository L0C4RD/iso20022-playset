# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import GeneralBusinessInformation1

class GeneralBusinessOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_GnlBiz"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@property
	def GnlBiz(self):
		return self._GnlBiz

	@GnlBiz.setter
	def GnlBiz(self, value):
		self._GnlBiz = value if value is not None else base_types.UninitialisedField(self, 'GnlBiz', GeneralBusinessInformation1, False)

	@GnlBiz.deleter
	def GnlBiz(self):
		del self._GnlBiz
		self._GnlBiz = base_types.UninitialisedField(self, 'GnlBiz', GeneralBusinessInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='GnlBiz', type=GeneralBusinessInformation1, min=0, max=1, mutex_group=1, array=False),
	))