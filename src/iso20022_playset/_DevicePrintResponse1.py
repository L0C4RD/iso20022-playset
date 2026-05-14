# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentType7Code import DocumentType7Code

class DevicePrintResponse1(base_types._BaseFieldType):

	__slots__ = ["_DocQlfr"]
	@property
	def DocQlfr(self):
		return self._DocQlfr

	@DocQlfr.setter
	def DocQlfr(self, value):
		self._DocQlfr = value if type(value) != base_types.auto else self.make_default("DocQlfr")

	@DocQlfr.deleter
	def DocQlfr(self):
		del self._DocQlfr
		self._DocQlfr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocQlfr', type=DocumentType7Code, min=1, max=1, mutex_group=None, array=False),
	))