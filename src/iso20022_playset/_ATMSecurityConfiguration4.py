# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm14Code
from . import Number

class ATMSecurityConfiguration4(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntrAlgo", "_MaxCerts", "_MaxSgntrs"]
	@property
	def DgtlSgntrAlgo(self):
		return self._DgtlSgntrAlgo

	@DgtlSgntrAlgo.setter
	def DgtlSgntrAlgo(self, value):
		self._DgtlSgntrAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntrAlgo', Algorithm14Code, True)

	@DgtlSgntrAlgo.deleter
	def DgtlSgntrAlgo(self):
		del self._DgtlSgntrAlgo
		self._DgtlSgntrAlgo = base_types.UninitialisedField(self, 'DgtlSgntrAlgo', Algorithm14Code, True)

	@property
	def MaxCerts(self):
		return self._MaxCerts

	@MaxCerts.setter
	def MaxCerts(self, value):
		self._MaxCerts = value if value is not None else base_types.UninitialisedField(self, 'MaxCerts', Number, False)

	@MaxCerts.deleter
	def MaxCerts(self):
		del self._MaxCerts
		self._MaxCerts = base_types.UninitialisedField(self, 'MaxCerts', Number, False)

	@property
	def MaxSgntrs(self):
		return self._MaxSgntrs

	@MaxSgntrs.setter
	def MaxSgntrs(self, value):
		self._MaxSgntrs = value if value is not None else base_types.UninitialisedField(self, 'MaxSgntrs', Number, False)

	@MaxSgntrs.deleter
	def MaxSgntrs(self):
		del self._MaxSgntrs
		self._MaxSgntrs = base_types.UninitialisedField(self, 'MaxSgntrs', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntrAlgo', type=Algorithm14Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxCerts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSgntrs', type=Number, min=0, max=1, mutex_group=None, array=False),
	))