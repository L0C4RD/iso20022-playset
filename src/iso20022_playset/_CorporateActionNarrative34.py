# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class CorporateActionNarrative34(base_types._BaseFieldType):

	__slots__ = ["_CertfctnBrkdwn", "_PtyCtctNrrtv", "_RegnDtls"]
	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwn")

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = None

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if type(value) != base_types.auto else self.make_default("PtyCtctNrrtv")

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = None

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != base_types.auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertfctnBrkdwn', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnDtls', type=RestrictedFINXMax350Text, min=0, max=None, mutex_group=None, array=True),
	))