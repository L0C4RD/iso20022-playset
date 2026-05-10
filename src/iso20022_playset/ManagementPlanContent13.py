import base_types
import Max140Binary
import Max10KBinary
import TMSAction13

class ManagementPlanContent13(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_TMChllng", "_KeyNcphrmntCert"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if type(value) != auto else self.make_default("TMChllng")

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = None

	@property
	def KeyNcphrmntCert(self):
		return self._KeyNcphrmntCert

	@KeyNcphrmntCert.setter
	def KeyNcphrmntCert(self, value):
		self._KeyNcphrmntCert = value if type(value) != auto else self.make_default("KeyNcphrmntCert")

	@KeyNcphrmntCert.deleter
	def KeyNcphrmntCert(self):
		del self._KeyNcphrmntCert
		self._KeyNcphrmntCert = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=TMSAction13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyNcphrmntCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
	))

