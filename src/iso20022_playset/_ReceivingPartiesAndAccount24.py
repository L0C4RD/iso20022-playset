# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentificationAndAccount235 import PartyIdentificationAndAccount235

class ReceivingPartiesAndAccount24(base_types._BaseFieldType):

	__slots__ = ["_RcvgAgtDtls", "_RcvrsCtdnDtls", "_RcvrsIntrmy1Dtls", "_RcvrsIntrmy2Dtls"]
	@property
	def RcvgAgtDtls(self):
		return self._RcvgAgtDtls

	@RcvgAgtDtls.setter
	def RcvgAgtDtls(self, value):
		self._RcvgAgtDtls = value if type(value) != base_types.auto else self.make_default("RcvgAgtDtls")

	@RcvgAgtDtls.deleter
	def RcvgAgtDtls(self):
		del self._RcvgAgtDtls
		self._RcvgAgtDtls = None

	@property
	def RcvrsCtdnDtls(self):
		return self._RcvrsCtdnDtls

	@RcvrsCtdnDtls.setter
	def RcvrsCtdnDtls(self, value):
		self._RcvrsCtdnDtls = value if type(value) != base_types.auto else self.make_default("RcvrsCtdnDtls")

	@RcvrsCtdnDtls.deleter
	def RcvrsCtdnDtls(self):
		del self._RcvrsCtdnDtls
		self._RcvrsCtdnDtls = None

	@property
	def RcvrsIntrmy1Dtls(self):
		return self._RcvrsIntrmy1Dtls

	@RcvrsIntrmy1Dtls.setter
	def RcvrsIntrmy1Dtls(self, value):
		self._RcvrsIntrmy1Dtls = value if type(value) != base_types.auto else self.make_default("RcvrsIntrmy1Dtls")

	@RcvrsIntrmy1Dtls.deleter
	def RcvrsIntrmy1Dtls(self):
		del self._RcvrsIntrmy1Dtls
		self._RcvrsIntrmy1Dtls = None

	@property
	def RcvrsIntrmy2Dtls(self):
		return self._RcvrsIntrmy2Dtls

	@RcvrsIntrmy2Dtls.setter
	def RcvrsIntrmy2Dtls(self, value):
		self._RcvrsIntrmy2Dtls = value if type(value) != base_types.auto else self.make_default("RcvrsIntrmy2Dtls")

	@RcvrsIntrmy2Dtls.deleter
	def RcvrsIntrmy2Dtls(self):
		del self._RcvrsIntrmy2Dtls
		self._RcvrsIntrmy2Dtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvgAgtDtls', type=PartyIdentificationAndAccount235, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsCtdnDtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsIntrmy1Dtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsIntrmy2Dtls', type=PartyIdentificationAndAccount235, min=0, max=1, mutex_group=None, array=False),
	))