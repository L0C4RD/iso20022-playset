# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationConfirmationV04 import ContractRegistrationConfirmationV04

class AUTH_019_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CtrctRegnConf"]
		@property
		def CtrctRegnConf(self):
			return self._CtrctRegnConf

		@CtrctRegnConf.setter
		def CtrctRegnConf(self, value):
			self._CtrctRegnConf = value if type(value) != base_types.auto else self.make_default("CtrctRegnConf")

		@CtrctRegnConf.deleter
		def CtrctRegnConf(self):
			del self._CtrctRegnConf
			self._CtrctRegnConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnConf', type=ContractRegistrationConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))