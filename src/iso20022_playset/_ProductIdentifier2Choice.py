# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification4
from . import ProductIdentifier2

class ProductIdentifier2Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctIdr", "_StrdPdctIdr"]
	@property
	def OthrPdctIdr(self):
		return self._OthrPdctIdr

	@OthrPdctIdr.setter
	def OthrPdctIdr(self, value):
		self._OthrPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'OthrPdctIdr', GenericIdentification4, False)

	@OthrPdctIdr.deleter
	def OthrPdctIdr(self):
		del self._OthrPdctIdr
		self._OthrPdctIdr = base_types.UninitialisedField(self, 'OthrPdctIdr', GenericIdentification4, False)

	@property
	def StrdPdctIdr(self):
		return self._StrdPdctIdr

	@StrdPdctIdr.setter
	def StrdPdctIdr(self, value):
		self._StrdPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'StrdPdctIdr', ProductIdentifier2, False)

	@StrdPdctIdr.deleter
	def StrdPdctIdr(self):
		del self._StrdPdctIdr
		self._StrdPdctIdr = base_types.UninitialisedField(self, 'StrdPdctIdr', ProductIdentifier2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctIdr', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctIdr', type=ProductIdentifier2, min=0, max=1, mutex_group=1, array=False),
	))